import urllib.request, re, ssl

ctx = ssl.create_default_context()
req = urllib.request.Request('https://travelens-frontend.onrender.com', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as r:
    html = r.read().decode('utf-8')

print('HTML:', html)
js_files = re.findall(r'src="(/assets/[^"]+\.js)"', html)
print('Found JS files:', js_files)
for js in js_files:
    js_url = 'https://travelens-frontend.onrender.com' + js
    req_js = urllib.request.Request(js_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req_js, context=ctx) as r_js:
        content = r_js.read().decode('utf-8')
    matches = re.findall(r'.{0,40}(?:travelens-backend|onrender\.com|/api|VITE_API).{0,40}', content)
    print(f'Matches in {js}:', len(matches))
    for m in matches[:10]:
        print('   ', m)
