# Loop through page to pull out links
def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
        
# Pass in page as string, and parse out html links in function
def get_next_target(page):
    start_link = page.find('<a href=')
    
    #If it is -1, means there were not links found in the string
    if (start_link == -1):
        return None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

#Define a function that grabs the html from a page and name it get_page.
#Until then, the below won't work unless page is set to html manually
print_all_links(get_page('http://xkcd.com/'))


                 

