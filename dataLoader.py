import pandas as pd
class DataLoader:
    """
    Dataloader
    """
    def __init__(self, filePath):
        """
        init and filter invalid data
        :param filePath: the path of the csv file
        """
        self.filePath = filePath
        self.data = pd.read_csv(filePath)
        self.data['Stars'] = self.data['Stars'].apply(lambda x: 0 if x=='Unrated' else float(x))

    def topReviewForEachItem(self):
        res = self.data.sort_values(by='Review #', ascending=False)
        return res

    def topReviewForEachBrand(self):
        """
        Top brands with the most popular ramens sorted by the number of review
        :return: DataFrame
        """
        res = self.data.groupby('Brand').agg({'Review #': 'sum'}).sort_values(by='Review #', ascending=False)
        return res

    def topStarForEachItem(self):
        """
        Top items sorted by stars
        :return: DataFrame
        """
        res = self.data.sort_values(by='Stars', ascending=False)
        return res


    def topMeanStarsForEachBrand(self):
        """
        Top brands with the most popular ramens sorted by mean of stars
        :return: DataFrame
        """
        res = self.data.groupby('Brand').agg({'Stars': 'mean'}).sort_values(by='Stars', ascending=False)
        return res

    def topSumStarsForEachBrand(self):
        """
        Top brands with the most popular ramens sorted by sum of stars
        :return: DataFrame
        """
        res = self.data.groupby('Brand').agg({'Stars': 'sum'}).sort_values(by='Stars', ascending=False)
        return res

    def topCountryForMeanStars(self):
        """
        Top countries with the most popular ramens sorted by mean of stars
        :return: DataFrame
        """
        res = self.data.groupby('Country').agg({'Stars': 'mean'}).sort_values(by='Stars', ascending=False)
        return res

    def StyleInCountry(self):
        """
        Record the number of each style consumed in each country
        dic[country][style] = a number
        :return: a dictionary
        """
        dic = {}
        for index, row in self.data.iterrows():
            if row['Country'] not in dic:
                dic[row['Country']] = {}
            else:
                dic[row['Country']][row['Style']] = dic[row['Country']].setdefault(row['Style'],0)+1
        return dic

    def TopStyleInCountry(self):
        """
        The most popular styles in each country
        :return: a dictionary
        """
        dic = self.StyleInCountry()
        res = {}
        for country, styles in dic.items():
            theMax = 0
            res[country] = []
            for style, number in styles.items():
                if number==theMax:
                    res[country].append((style,number))
                elif number>theMax:
                    theMax = number
                    res[country].clear()
                    res[country].append((style, number))
        return res

path = './ramen-ratings.csv'
test = DataLoader(path)
print(test.TopStyleInCountry())