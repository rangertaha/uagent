

Random User Agent Strings
===========

This module allows you to a random user string from the specified category.

Categories of User Agents
-----------------------

    * Browsers
    * Mobile
    * Libraries
    * Crawlers
    * Validators
    * Email Clients
    * Link Checkers
    * Offline
    * Others




UA = {'libraries': LIBRARIES, 'crawlers': CRAWLERS, 'others': OTHER,
      'email_clients': EMAIL_CLIENTS, 'link_checkers': LINK_CHECKERS,
      'mobile': MOBILE, 'validators': VALIDATORS, 'offline': OFFLINE,
      'feed_readers': FEED_READERS, 'browsers': BROWSERS}

Example
-------


    from uagent import UserAgent

    # Returns random user agent
    UserAgnet()

    # Returns random user agent used by web browsers
    UserAgent('browsers')

    # Returns random user agent used by web crawlers
    UserAgent('crawlers')


