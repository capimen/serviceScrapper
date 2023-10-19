import json

class Comparator:

    def __init__(self, id, id_product, product_name, price_newest, price_average, price_best,
                 price_worst, discount_priceleft, discount_percent, average_safe, average_safe_worst,
                 diff_best, url, best_historical_flag, umbral, umbral_flag, reg_date, umbral_priceReference):
        self.id = id
        self.id_product = id_product
        self.product_name  = product_name
        self.price_newest = price_newest
        self.price_average = price_average
        self.price_best = price_best
        self.price_worst = price_worst
        self.discount_priceleft = discount_priceleft
        self.discount_percent = discount_percent
        self.average_safe = average_safe
        self.average_safe_worst = average_safe_worst
        self.diff_best = diff_best
        self.url = url
        self.best_historical_flag = best_historical_flag
        self.umbral = umbral
        self.umbral_flag = umbral_flag
        self.reg_date = reg_date
        self.umbral_priceReference = umbral_priceReference

    @classmethod
    def fromJson(self, jsonComnparator):

        self.id = jsonComnparator['id']
        self.id_product = jsonComnparator['id_product']
        self.product_name  = jsonComnparator['product_name']
        self.price_newest = jsonComnparator['price_newest']
        self.price_average = jsonComnparator['price_average']
        self.price_best = jsonComnparator['price_best']
        self.price_worst = jsonComnparator['price_worst']
        self.discount_priceleft = jsonComnparator['discount_priceleft']
        self.discount_percent = jsonComnparator['discount_percent']
        self.average_safe = jsonComnparator['average_safe']
        self.average_safe_worst = jsonComnparator['average_safe_worst']
        self.diff_best = jsonComnparator['diff_best']
        self.url = jsonComnparator['url']
        self.best_historical_flag = jsonComnparator['best_historical_flag']
        self.umbral = jsonComnparator['umbral']
        self.umbral_flag = jsonComnparator['umbral_flag']
        self.reg_date = jsonComnparator['reg_date']
        self.umbral_priceReference = jsonComnparator['umbral_priceReference']
        return self

    def toJson(self):
        arr = {}
        arr['id'] = self.id
        arr['id_product'] = self.id_product
        arr['product_name']  = self.product_name
        arr['price_newest'] = self.price_newest
        arr['price_average'] = self.price_average
        arr['price_best'] = self.price_best
        arr['price_worst'] = self.price_worst
        arr['discount_priceleft'] = self.discount_priceleft
        arr['discount_percent'] = self.discount_percent
        arr['average_safe'] = self.average_safe
        arr['average_safe_worst'] = self.average_safe_worst
        arr['diff_best'] = self.diff_best
        arr['url'] = self.url
        arr['best_historical_flag'] = self.best_historical_flag
        arr['umbral'] = self.umbral
        arr['umbral_flag'] = self.umbral_flag
        arr['reg_date'] = self.reg_date
        arr['umbral_priceReference'] = self.umbral_priceReference
        return json.dumps(arr)

    def toList(self):
        arr = {}
        arr['id'] = self.id
        arr['id_product'] = self.id_product
        arr['product_name']  = self.product_name
        arr['price_newest'] = self.price_newest
        arr['price_average'] = self.price_average
        arr['price_best'] = self.price_best
        arr['price_worst'] = self.price_worst
        arr['discount_priceleft'] = self.discount_priceleft
        arr['discount_percent'] = self.discount_percent
        arr['average_safe'] = self.average_safe
        arr['average_safe_worst'] = self.average_safe_worst
        arr['diff_best'] = self.diff_best
        arr['url'] = self.url
        arr['best_historical_flag'] = self.best_historical_flag
        arr['umbral'] = self.umbral
        arr['umbral_flag'] = self.umbral_flag
        arr['reg_date'] = self.reg_date
        arr['umbral_priceReference'] = self.umbral_priceReference
        return arr

    def toArray(self):
        arr = []
        arr.append(self.id)
        arr.append(self.id_product)
        arr.append(self.product_name)
        arr.append(self.price_newest)
        arr.append(self.price_average)
        arr.append(self.price_best)
        arr.append(self.price_worst)
        arr.append(self.discount_priceleft)
        arr.append(self.discount_percent)
        arr.append(self.average_safe)
        arr.append(self.average_safe_worst)
        arr.append(self.diff_best)
        arr.append(self.url)
        arr.append(self.best_historical_flag)
        arr.append(self.umbral)
        arr.append(self.umbral_flag)
        arr.append(self.reg_date)
        arr.append(self.umbral_priceReference)
        return arr


    def print(self):
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))

