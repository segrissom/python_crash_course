#This is exercise 11 from chapter 6 of Python Crash Course
cities={
    "Kyoto": {
        "Country": "Japan",
        "Population": '1.5 Million',
        "Fact": "it used to be the capital city of Japan."
    },
    "New York City": {
        "Country":"United States",
        "Population":'8+ million',
        "Fact":"that is the most populous city in the United States."
    },
    "Hong Kong":{
        "Country":'Hong Kong Special Administrative Region of the People\'s Republic of China',
        "Population":'7.4 million',
        "Fact": "was formerly owned by Britain"
    }
}
for city, facts in cities.items():
    print(city.title() + " has many interesting things about it.")
    print("It's located in " + facts['Country']+ " with a population of " + facts['Population']+".")
    print("An interesting fact about it is "+ facts['Fact']+".")
