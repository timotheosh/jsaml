all:
	mkdir target && \
	cd target && \
	nuitka3 --standalone --static-libpython=no --python-flag=no_site --clang ../jsaml/jsaml.py

clean:
	rm -rf target/ 
