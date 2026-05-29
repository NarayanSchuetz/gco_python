GCO_SHA256 = 7562be2fa7ef19404a24a29d15414b949bdcab785370479ecc3a57a8f1cfb538

gco_python: gco_src
	python setup.py build_ext -i

gco-v3.0.zip:
	wget https://vision.cs.uwaterloo.ca/files/gco-v3.0.zip
	echo "$(GCO_SHA256)  gco-v3.0.zip" | sha256sum -c -

gco_src: gco-v3.0.zip
	mkdir gco_src
	cd gco_src && unzip ../gco-v3.0.zip
