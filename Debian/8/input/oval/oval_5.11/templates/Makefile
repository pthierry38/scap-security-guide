SHARED_DIR:=../../../../../../shared/oval/templates
OUTPUT:=$(shell mkdir -p output)

all:
	${SHARED_DIR}/create_services_enabled.py services_enabled.csv
	${SHARED_DIR}/create_services_disabled.py services_disabled.csv

copy: postbuild
	cp output/*.xml ..

# some shared oval need postbuild update.
postbuild:
#	ssh service is named ssh in Debian, not sshd, updating oval id.
	sed -re 's:service_ssh_disabled:service_sshd_disabled:g' -i output/service_ssh_disabled.xml

clean:
	rm -rf output/*.xml
	rm -rf output/*.sh
	rm -rf output
