import textwrap
sample_text = '''
    Currently the techniques followed in agriculture are obsolete and of no use. 
    We follow the same techniques that were followed by our ancestors 20-25 years ago. 
    But the climate and weather conditions have changed drastically, pollution has increased on 
    on uncountable scale that's why the net average production per hectare of India is also decreasing day by day. 
    Their are proven reports for example taking case of Ethiopia, where when appropriate amount of NPK
    was used and proper soil testing was done to grow maize , their net average production reached
    around 6-7 tons per hectare that is somewhere equal to the European average. But in India it's not
    that easy or feasible to approach a small farmer to tell him to get his soil tested. As in India small
    farmers don't have 500-600 bucks, to buy seeds then why will he listen to us to get his soil tested. 
    So making sure that it's
    within his reach will ensure that he would in fact listen to us but would also take the advice.
    '''
new_text = textwrap.dedent(sample_text)
print()
print(new_text )
print()