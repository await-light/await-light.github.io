template = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1">
	<link rel="stylesheet" href="/static/styles.css">
	<script src="/static/common.js"></script>
	<title></title>
</head>
<body>
	<iframe src frameborder="0" width="100%" height="100%" scrolling="no"></iframe>
</body>
</html>
"""

platforms = ["goofish", "jym", "zz"]
custaccs = [f"cust{i}" for i in range(1, 51)]

for pf in platforms:
	for ca in custaccs:
		with open(f"{pf}/{ca}.html", "w") as f:
			f.write(template)