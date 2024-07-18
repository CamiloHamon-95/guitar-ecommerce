def get_favs(favorites):
    fav_list= []
    myfavs = favorites.replace('{','')
    myfavs = myfavs.replace('}','')
    myfavs = myfavs.replace('"','')
    fav_guitars = myfavs.split(',')
    
    for fav_one in fav_guitars:
        fav_list.append(fav_one.split(':'))
    
    return dict(fav_list)