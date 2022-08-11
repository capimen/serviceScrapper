#import mysql.connector
import pymysql

class SqlHelper:

    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="password",
            database="scraper"
        )
        self.mycursor = self.db.cursor()

#CRUD PRODUCT
    def select_product(self):
        query = "select	   p.id," \
                "          p.name, " \
                "          p.reference_price, " \
                "          p.id_category, " \
                "          p.img_url, " \
                "          p.status " \
                "from  	   product p " \
                "order by p.id_category asc, " \
                "          p.id asc;"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def select_product_by_id(self, id):
        query = "select	   p.id," \
                "          p.name, " \
                "          p.reference_price, " \
                "          p.id_Category, " \
                "          p.img_Url, " \
                "          p.status " \
                "from  	   product p  " \
                "where     p.id = " + str(id) + " ;"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def update_product(self, product):

        #esto es para cambiar el None del codigo a null de la base de datos
        if product.imgUrl == None:

            product.imgUrl = "null"

        else:

            product.imgUrl = str("'"+product.imgUrl+"'")

        query = " UPDATE product " \
                " SET " \
                " name = '" + product.name + "'," \
                " reference_price = " + product.referencePrice + "',"\
                " id_category = " + str(product.idCategory) + ", " \
                " img_url = " + product.imgUrl + ", " \
                " status = " + str(product.status) + " " \
                " WHERE id = " + str(product.id) + "; "
        self.mycursor.execute(query)
        self.mycursor.execute("commit;")

    def insert_product(self, product):

        #esto es para cambiar el None del codigo a null de la base de datos
        if product.imgUrl == None:

            product.imgUrl = "null"

        else:

            product.imgUrl = str("'"+product.imgUrl+"'")

        query = " INSERT INTO product " \
                " ( " \
                " name, " \
                " reference_price, " \
                " id_category, " \
                " img_url, " \
                " status" \
                " ) " \
                " VALUES " \
                " ( " \
                " '" + product.name + "'," \
                " " + str(product.referencePrice) + "," \
                " " + str(product.idCategory) + "," \
                " " + product.imgUrl + "," \
                " " + str(product.status) + "" \
                " ); "
        self.mycursor.execute(query)
        self.mycursor.execute("commit;")


#CRUD PRODUCT_COMMERCE-DETAIL
    def insert_product_commerce_detail(self, productCommerceDetail):

        query = "INSERT INTO product_commerce_detail " \
                "    ( " \
                "        id_product," \
                "        id_commerce," \
                "        url" \
                "    ) " \
                "    VALUES" \
                "    ( " \
                "         " + str(productCommerceDetail.idProduct) + ", " \
                "         " + str(productCommerceDetail.idCommerce)+", " \
                "         " + str(productCommerceDetail.url)+ "" \
                "    );"

        self.mycursor.execute(query)
        self.mycursor.execute("commit;")

    def select_commerce_by_id(self, idCommerce):

        query = "select	    c.id, " \
                "           c.name, " \
                "           c.priceclass, " \
                "           c.pricetag, " \
                "           c.nameclass, " \
                "           c.nametag " \
                "from   commerce " \
                "where id = " + str(idCommerce) + ";"

        self.mycursor.execute(query)
        return self.mycursor.fetchall()


#CRUD COMMMERCE
    def insert_commerce(self, commerce):

        query = " INSERT INTO `scraper`.`commerce` " \
                "   ( " \
                "   name, " \
                "   priceclass, " \
                "   pricetag, " \
                "   nameclass, " \
                "   nametag " \
                "   ) " \
                " VALUES " \
                "   ( " \
                "   '" + commerce.name + "', " \
                "   '" + commerce.priceclass + "', " \
                "   '" + commerce.pricetag + "', " \
                "   '" + commerce.nameclass + "', " \
                "   '" + commerce.nametag + "' " \
                "   );"

        self.mycursor.execute(query)
        self.mycursor.execute("commit;")

    def select_commerce(self):
        query = " select " \
                "   c.id, " \
                "   c.name, " \
                "   c.priceclass, " \
                "   c.pricetag, " \
                "   c.nameclass, " \
                "   c.nametag " \
                " from  commerce c; "

        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    # olds

    def update_product_name(self,productScraped):

        query = "UPDATE `scraper`.`product` " \
                "SET `name` = \""+ productScraped.productName +"\" " \
                "WHERE `id` = "+str(productScraped.productId)+";"
        self.mycursor.execute(query)
        self.mycursor.execute("commit;")


    def select_get_productHistorical(self, rowPid):
        query = "select    h.price, " \
		        "          d.url, " \
                "          h.id_product, " \
                "          c.name, " \
                "          c.id " \
                "from	   historical h, " \
		        "          product_commerce_detail d, " \
                "          commerce c " \
                "where 	   h.id_product = " + str(rowPid) + " " \
                "and	   h.id_product = d.id_product " \
                "and		h.id_commerce = d.id_commerce " \
                "and		d.id_commerce = c.id " \
                "order by h.reg_date desc " \
                "limit 1 "
        self.mycursor.execute(query)
        return self.mycursor.fetchall()


    def select_init(self):

        query = "select   p.id, " \
                "         d.url, " \
                "         c.name, " \
                "         c.priceclass, " \
                "         c.pricetag, " \
                "         c.nameclass, " \
                "         c.nametag," \
                "         c.id , " \
                "         d.id " \
                "from     product p, " \
                "         commerce c, " \
                "         product_commerce_detail d " \
                "where    p.id = d.id_product " \
                "and      p.status = 1 " \
                "and      c.id = d.id_commerce " \

        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    #Comparador
    def select_get_priceAverage(self,rowPid,rowCid):

        query = "select 	avg(h.price) " \
                "from 	historical h " \
                "where 	id_product = " + str(rowPid) + " " \
                "and    id_commerce = " + str(rowCid) + ";"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()


    def select_get_bestprice(self, rowPid,rowCid):

        query = "select 	h.price " \
                "from    historical h " \
                "where 	id_product = " + str(rowPid) + " " \
                "and    id_commerce = " + str(rowCid) + " " \
                "and 	h.price is not null " \
                "order by h.price " \
                "asc limit 1; "
        self.mycursor.execute(query)
        return self.mycursor.fetchall()


    def select_get_worstprice(self, rowPid,rowCid):

        query = "select h.price " \
               "from   historical h " \
               "where 	id_product = " + str(rowPid) + " " \
               "and    id_commerce = " + str(rowCid) + " " \
               "order by h.price " \
               "desc limit 1; "
        self.mycursor.execute(query)
        return self.mycursor.fetchall()


    def select_get_newestprice(self, rowPid, rowCid):

        query = "select 	h.price " \
                "from 	    historical h " \
                "where 	id_product = " + str(rowPid) + " " \
                "and    id_commerce = " + str(rowCid) + " " \
                "order by h.reg_date " \
                "desc limit 1; "
        self.mycursor.execute(query)
        return self.mycursor.fetchall()


    def insert_historical(self, productScraped):

        query = "INSERT INTO `scraper`.`historical` " \
                "(" \
                "`id_product`," \
                "`price`, " \
                "`id_commerce`, " \
                "`id_product_commerce_detail` " \
                ") " \
                "VALUES " \
                "(" \
                " " + str(productScraped.productId) + " , " \
                " " + productScraped.valor + " , " \
                " " + str(productScraped.commerceId) + " , " \
                " " + str(productScraped.productCommerceDetailId) + "  " \
                "); "
        self.mycursor.execute(query)
        self.mycursor.execute("commit;")



    def select_pending (self):

        query = "select   p.id, " \
                "         d.url, " \
                "         c.name, " \
                "         c.priceclass, " \
                "         c.pricetag, " \
                "         c.nameclass, " \
                "         c.nametag," \
                "         c.id , " \
                "         d.id " \
                "from     product p, " \
                "         commerce c, " \
                "         product_commerce_detail d " \
                "where    p.id = d.id_product " \
                "and      p.status = 1 " \
                "and      c.id = d.id_commerce " \
                "and 	  d.id not in ( " \
                "   select h.id_product_commerce_detail " \
                "	from historical h " \
                "   where h.reg_date > curdate() " \
                "); "
        self.mycursor.execute(query)
        return self.mycursor.fetchall()
#"   where h.reg_date > curdate() " \

    def truncate_comparator(self):

        query = "truncate table `scraper`.`comparator`; "
        self.mycursor.execute(query)
        self.mycursor.execute("commit;")


    def insert_comparator(self, productHistoricalInfo):

        query = "INSERT INTO `scraper`.`comparator` " \
                "(" \
                "`product_id`," \
                "`product_name` ," \
                "`price_newest`," \
                "`price_average`," \
                "`price_best`," \
                "`price_worst`," \
                "`discount_priceleft`," \
                "`discount_percent`," \
                "`average_safe`," \
                "`average_safe_worst`," \
                "`diff_best`," \
                "`url`," \
                "`best_historical_flag`," \
                "`umbral`," \
                "`umbral_flag`" \
                ")" \
                "VALUE" \
                "(" \
                "" + str(productHistoricalInfo.id) + "," \
                " \"" + productHistoricalInfo.name + "\"," \
                "" + str(int(productHistoricalInfo.priceNewest)) + "," \
                "" + str(int(productHistoricalInfo.priceAverage)) + "," \
                "" + str(int(productHistoricalInfo.priceBest)) + "," \
                "" + str(int(productHistoricalInfo.priceWorst)) + "," \
                "" + str(productHistoricalInfo.percentPrice) + "," \
                "" + str(productHistoricalInfo.priceDiscountPercent) + "," \
                "" + str(int(productHistoricalInfo.priceAverage) - int(productHistoricalInfo.priceNewest)) + "," \
                "" + str(int(productHistoricalInfo.priceWorst) - int(productHistoricalInfo.priceNewest)) + "," \
                "" + str(int(productHistoricalInfo.priceBest) - int(productHistoricalInfo.priceNewest)) + "," \
                " \"" + productHistoricalInfo.url + "\"," \
                "" + str(productHistoricalInfo.historicalBestFlag) + ", " \
                "" + str(productHistoricalInfo.umbral) + ", " \
                "" + str(productHistoricalInfo.umbralFlag) + " "\
                ");"
        self.mycursor.execute(query)
        self.mycursor.execute("commit;")


    def select_comparator(self):
        query = "SELECT id," \
                "       product_id," \
                "       product_name," \
                "       price_newest," \
                "       price_average," \
                "       price_best," \
                "       price_worst," \
                "       discount_priceleft," \
                "       discount_percent," \
                "       average_safe," \
                "       average_safe_worst," \
                "       diff_best," \
                "       url," \
                "       best_historical_flag," \
                "       reg_date " \
                "FROM `scraper`.`comparator`;"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()


#deprecated

    def select_get_product_deprecated(self):
        query = "select	   p.id," \
                "          p.name, " \
                "          p.reference_price, " \
                "          g.discount, " \
                "          g.name " \
                "from  	   product p, " \
                "          category g " \
                "where     p.id_category = g.id " \
                "and       p.status = 1 " \
                "order by p.id_category asc, " \
                "          p.id asc;"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def select_get_product_by_id_deprecated(self, id):
        query = "select	   p.id," \
                "          p.name, " \
                "          p.reference_price, " \
                "          g.discount, " \
                "          g.name " \
                "from  	   product p, " \
                "          category g " \
                "where     p.id_category = g.id " \
                "and       p.status = 1 " \
                "and       p.id = " + str(id) + " ;"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

