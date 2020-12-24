'''module for object in home'''
class BadMentalHealth:
    '''Class Model for symptoms'''
    def __init__(self, name, desc, image, symptom, desctom): # pylint: disable=too-many-arguments
        self.name = name
        self.desc = desc
        self.image = image
        self.symptom = symptom
        self.desctom = desctom

class Symptoms: # pylint: disable=too-few-public-methods
    '''List of Symptom'''
    bipolar_name1 = 'Bipolar I disorder'
    bipolar_name2 = 'Bipolar II disorder'
    bipolar_name3 = 'Cyclothymic disorder'
    bipolar_name4 = 'Other types'

    bipolar_desc1 = 'You"ve had at least one manic episode that may be preceded or followed by hypomanic or major depressive episodes.' # pylint: disable=line-too-long
    bipolar_desc2 = 'You"ve had at least one major depressive episode and at least one hypomanic episode, but you"ve never had a manic episode.' # pylint: disable=line-too-long
    bipolar_desc3 = 'You"ve had at least two years — or one year in children and teenagers — of many periods of hypomania symptoms and periods of depressive symptoms (though less severe than major depression).' # pylint: disable=line-too-long
    bipolar_desc4 = 'These include, for example, bipolar and related disorders induced by certain drugs or alcohol or due to a medical condition, such as Cushing"s disease, multiple sclerosis or stroke.' # pylint: disable=line-too-long

    stress_name1 = 'Headaches'

    stress_desc1 = 'Other common headache triggers include lack of sleep, alcohol consumption and dehydration.' # pylint: disable=line-too-long
class CareUTeam:
    '''object team careu'''
    def __init__(self, name, npm, url, image):
        self.name = name
        self.npm = npm
        self.url = url
        self.image = image
