Random User Agent Strings
===========

This module allows you to select a random user agent from a list of categories. All categories total to 10886 user agent strings.

Categories of User Agent Strings
-----------------------



* 9420   Browsers
* 508    Mobile
* 141 Libraries
* 442 Crawlers
* 17 Validators
* 217 Email Clients
* 13 Feed Readers
* 34 Link Checkers
* 34 Offline
* 60 Others


Example
-------

The following example selects a random user agent from all the categories.

    from uagent import UserAgent

    uas = UserAgnet()

    # Returns random user agent, selected from all the categories
    ua = uas.random()


Browsers
________

	# Initialize and select the 'browsers' category
	uas = UserAgent('browsers')

    # Returns random user agent from this category
    ua = uas.random()
