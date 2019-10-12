from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
import operator
import pandas as pd

#Directs to default HTML page for search of word
def fuzzySearch(request):
    return render(request, 'fuzzyIndex.html', {})


#This method for reading the file and Storing word and frequnecy of word. When user starts entering a word/char in
# text box, it searches for a char/word on every input and returns the matching list of words to user.
def checkOccurence(partialword):
    #used pandas library to read dataset of csv
    # for TSV file sep parameter given as '\t'
    data = pd.read_csv("./fuzzy_search.csv", engine='python', sep=None,
                       encoding='utf-8')
    #Dict to store word and frequency
    totalwordcount = dict(zip(data['name'],data['frequency']))
    wordsList = list(data['name'])

    #Checking each input present in dataset
    results = []
    for i in range(len(wordsList)):
        if str(partialword) in str(wordsList[i]):
            results.append(str(wordsList[i]))
        else:pass
    #All input matching words stored in 'result' list

    # 'rank' sorts the list of matching word based in the frequency and length of word. Shorter match has higher
    # frequency than the longer
    ranks = [(result, result.find(str(partialword)), totalwordcount[result], len(result)) for result in
                        results]
    ranks.sort(key=operator.itemgetter(1))
    ranks.sort(key=operator.itemgetter(3))
    finalResults = [ranks[0] for ranks in ranks][:25]
    return finalResults


#Returns the autocomplete results while the user types in a letter.
def fuzzyAutoComp(request):
    word = request.GET.get('term','')
    finalWord = checkOccurence(word.lower())
    data = json.dumps(finalWord)
    return HttpResponse(data,'application/json')

#On Click of submit button return 25 matching result in Json format
def getResult(request):
    if request.method == 'GET':
        word = request.GET.get('word') # for example: query = 'hello'
        if word:
            finalWord = checkOccurence(word.lower())
            if len(finalWord) > 0:
                return JsonResponse({'Matches': finalWord})
            else:return JsonResponse({'Matches': "No Suggestion Found"})
        else:
            return redirect('/')
