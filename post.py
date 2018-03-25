import facebook

def main():
	cfg = {
		"page_id" : "324636527678327", 
		"access_token" : "EAAbZAN5ijk70BALz5roZCHClCdgaSZBrGpTAr5CGczu9ZAso7YvqkshNFjl65yNZCZCmZCsgZBVSAO52V3hJ102sEltfrTuUW0ZBu9TXSDhHd7QPI5X5qZAD11YlkXx9aG20DK2jGZB8v3kwwHCUDZBitZAjceZB02V7SjJx9WomGvpDihHVGEEWPn4deEarCVCW5JOADAbdctBIiXngZDZD"
		}
		
	api = get_api(cfg)
	msg = "Hello, world!"
	status = api.put_wall_post(msg)
	return status
  
def get_api(cfg):
	graph = facebook.GraphAPI(cfg['access_token'])
	# Get page token to post as the page. You can skip 
	# the following if you want to post as yourself. 
	resp = graph.get_object('me/accounts')
	page_access_token = None
	for page in resp['data']:
		if page['id'] == cfg['page_id']:
			page_access_token = page['access_token']
	graph = facebook.GraphAPI(page_access_token)
	return graph
	
if __name__ == "__main__":
	main()