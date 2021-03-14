import pprint
import veryfi

client_id = "vrfxsM22WVr6PHhM8AsUd7b2np7jUE52PrgHT8v"
client_secret = 'caO4ZDFhvJIrx6W52LBYNSUAhwGWVyLe189bUriI14NOpfFyoSRLbk23W7mPfIyUbSvIdA6IjuRZBGA7eLMx4Ec0SZiaACkPntfYmdNgol8SzA1k6dopenXMnD0y8c0I'
username = 'satu.dua.tiga6'
api_key = '2f4ddb23937bf17dce6cb2ab2e0e6328'

client = veryfi.Client(client_id, client_secret, username, api_key)

file_path ="UnReadable_Continue\1.pdf"
json_result = client.process_document(file_path)

pprint.pprint(json_result)