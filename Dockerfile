FROM odoo:16.0

USER root

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8
#USER odoo
#RUN mkdir /backup
#RUN chown -R odoo: /backup

#COPY /mnt/extra-addons/sudestada/sudestada_filestore/* /backup
#USER root
RUN apt-get update
RUN apt-get install --assume-yes --no-install-recommends --quiet \
        python3 python3-dev python2.7-dev \
        python3-pip \
        libldap2-dev libsasl2-dev slapd ldap-utils tox lcov valgrind \
    && apt-get clean all

COPY requirements.txt ./

RUN pip3 install --upgrade pip
RUN pip3 install -r  requirements.txt


RUN chown -R odoo: /var/lib/odoo
RUN rm -rf /mnt/extra-addons/
USER odoo
COPY ./etc/config /etc/odoo/
WORKDIR /mnt/extra-addons
COPY  . ./odoo16

USER root
#RUN chown -R odoo: /mnt/extra-addons/sudestada/sudestada_filestore
#COPY ./backup/ /mnt/extra-addons/sudestada/sudestada_filestore
#RUN CHMOD 777 -R /mnt/extra-addons/sudestada/sudestada_filestore