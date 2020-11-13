from collections import defaultdict

# from typing import Callable
# import re
# from typing import Dict, Any, List

# import requests
# from bs4 import BeautifulSoup, Comment

# PARSER = 'lxml'


class UnknownVenueError(Exception):
    @staticmethod
    def unknown_venue():
        raise UnknownVenueError('Unknown venue')


VENUE_URLS = defaultdict(
    UnknownVenueError.unknown_venue,
    {
        'usenix2000': 'https://dblp.org/db/conf/uss/uss2000.html',
        'usenix2001': 'https://dblp.org/db/conf/uss/uss2001.html',
        'usenix2002': 'https://dblp.org/db/conf/uss/uss2002.html',
        'usenix2003': 'https://dblp.org/db/conf/uss/uss2003.html',
        'usenix2004': 'https://dblp.org/db/conf/uss/uss2004.html',
        'usenix2005': 'https://dblp.org/db/conf/uss/uss2005.html',
        'usenix2006': 'https://dblp.org/db/conf/uss/uss2006.html',
        'usenix2007': 'https://dblp.org/db/conf/uss/uss2007.html',
        'usenix2008': 'https://dblp.org/db/conf/uss/uss2008.html',
        'usenix2009': 'https://dblp.org/db/conf/uss/uss2009.html',
        'usenix2010': 'https://dblp.org/db/conf/uss/uss2010.html',
        'usenix2011': 'https://dblp.org/db/conf/uss/uss2011.html',
        'usenix2012': 'https://dblp.org/db/conf/uss/uss2012.html',
        'usenix2013': 'https://dblp.org/db/conf/uss/uss2013.html',
        'usenix2014': 'https://dblp.org/db/conf/uss/uss2014.html',
        'usenix2015': 'https://dblp.org/db/conf/uss/uss2015.html',
        'usenix2016': 'https://dblp.org/db/conf/uss/uss2016.html',
        'usenix2017': 'https://dblp.org/db/conf/uss/uss2017.html',
        'usenix2018': 'https://dblp.org/db/conf/uss/uss2018.html',
        'usenix2019': 'https://dblp.org/db/conf/uss/uss2019.html',
        'usenix2020': 'https://dblp.org/db/conf/uss/uss2020.html',
        'ndss2000': 'https://dblp.org/db/conf/ndss/ndss2000.html',
        'ndss2001': 'https://dblp.org/db/conf/ndss/ndss2001.html',
        'ndss2002': 'https://dblp.org/db/conf/ndss/ndss2002.html',
        'ndss2003': 'https://dblp.org/db/conf/ndss/ndss2003.html',
        'ndss2004': 'https://dblp.org/db/conf/ndss/ndss2004.html',
        'ndss2005': 'https://dblp.org/db/conf/ndss/ndss2005.html',
        'ndss2006': 'https://dblp.org/db/conf/ndss/ndss2006.html',
        'ndss2007': 'https://dblp.org/db/conf/ndss/ndss2007.html',
        'ndss2008': 'https://dblp.org/db/conf/ndss/ndss2008.html',
        'ndss2009': 'https://dblp.org/db/conf/ndss/ndss2009.html',
        'ndss2010': 'https://dblp.org/db/conf/ndss/ndss2010.html',
        'ndss2011': 'https://dblp.org/db/conf/ndss/ndss2011.html',
        'ndss2012': 'https://dblp.org/db/conf/ndss/ndss2012.html',
        'ndss2013': 'https://dblp.org/db/conf/ndss/ndss2013.html',
        'ndss2014': 'https://dblp.org/db/conf/ndss/ndss2014.html',
        'ndss2015': 'https://dblp.org/db/conf/ndss/ndss2015.html',
        'ndss2016': 'https://dblp.org/db/conf/ndss/ndss2016.html',
        'ndss2017': 'https://dblp.org/db/conf/ndss/ndss2017.html',
        'ndss2018': 'https://dblp.org/db/conf/ndss/ndss2018.html',
        'ndss2019': 'https://dblp.org/db/conf/ndss/ndss2019.html',
        'ndss2020': 'https://dblp.org/db/conf/ndss/ndss2020.html',
        'ccs2000': 'https://dblp.org/db/conf/ccs/ccs2000.html',
        'ccs2001': 'https://dblp.org/db/conf/ccs/ccs2001.html',
        'ccs2002': 'https://dblp.org/db/conf/ccs/ccs2002.html',
        'ccs2003': 'https://dblp.org/db/conf/ccs/ccs2003.html',
        'ccs2004': 'https://dblp.org/db/conf/ccs/ccs2004.html',
        'ccs2005': 'https://dblp.org/db/conf/ccs/ccs2005.html',
        'ccs2006': 'https://dblp.org/db/conf/ccs/ccs2006.html',
        'ccs2007': 'https://dblp.org/db/conf/ccs/ccs2007.html',
        'ccs2008': 'https://dblp.org/db/conf/ccs/ccs2008.html',
        'ccs2009': 'https://dblp.org/db/conf/ccs/ccs2009.html',
        'ccs2010': 'https://dblp.org/db/conf/ccs/ccs2010.html',
        'ccs2011': 'https://dblp.org/db/conf/ccs/ccs2011.html',
        'ccs2012': 'https://dblp.org/db/conf/ccs/ccs2012.html',
        'ccs2013': 'https://dblp.org/db/conf/ccs/ccs2013.html',
        'ccs2014': 'https://dblp.org/db/conf/ccs/ccs2014.html',
        'ccs2015': 'https://dblp.org/db/conf/ccs/ccs2015.html',
        'ccs2016': 'https://dblp.org/db/conf/ccs/ccs2016.html',
        'ccs2017': 'https://dblp.org/db/conf/ccs/ccs2017.html',
        'ccs2018': 'https://dblp.org/db/conf/ccs/ccs2018.html',
        'ccs2019': 'https://dblp.org/db/conf/ccs/ccs2019.html',
        'ccs2020': 'https://dblp.org/db/conf/ccs/ccs2020.html',
        'oakland2000': 'https://dblp.org/db/conf/sp/sp2000.html',
        'oakland2001': 'https://dblp.org/db/conf/sp/sp2001.html',
        'oakland2002': 'https://dblp.org/db/conf/sp/sp2002.html',
        'oakland2003': 'https://dblp.org/db/conf/sp/sp2003.html',
        'oakland2004': 'https://dblp.org/db/conf/sp/sp2004.html',
        'oakland2005': 'https://dblp.org/db/conf/sp/sp2005.html',
        'oakland2006': 'https://dblp.org/db/conf/sp/sp2006.html',
        'oakland2007': 'https://dblp.org/db/conf/sp/sp2007.html',
        'oakland2008': 'https://dblp.org/db/conf/sp/sp2008.html',
        'oakland2009': 'https://dblp.org/db/conf/sp/sp2009.html',
        'oakland2010': 'https://dblp.org/db/conf/sp/sp2010.html',
        'oakland2011': 'https://dblp.org/db/conf/sp/sp2011.html',
        'oakland2012': 'https://dblp.org/db/conf/sp/sp2012.html',
        'oakland2013': 'https://dblp.org/db/conf/sp/sp2013.html',
        'oakland2014': 'https://dblp.org/db/conf/sp/sp2014.html',
        'oakland2015': 'https://dblp.org/db/conf/sp/sp2015.html',
        'oakland2016': 'https://dblp.org/db/conf/sp/sp2016.html',
        'oakland2017': 'https://dblp.org/db/conf/sp/sp2017.html',
        'oakland2018': 'https://dblp.org/db/conf/sp/sp2018.html',
        'oakland2019': 'https://dblp.org/db/conf/sp/sp2019.html',
        'oakland2020': 'https://dblp.org/db/conf/sp/sp2020.html',
    },
)
