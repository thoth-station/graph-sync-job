FROM fedora:27
CMD ["sync"]
ENTRYPOINT ["/workdir/app.py"]
ENV \
 LANG=en_US.UTF-8 \
 THOTH_GRAPH_SYNC_DIR='/workdir'

COPY ./ ${THOTH_GRAPH_SYNC_DIR}
RUN \
 mkdir -p ${THOTH_GRAPH_SYNC_DIR} &&\
 cd ${THOTH_GRAPH_SYNC_DIR} &&\
 pip3 install -r requirements.txt &&\
 # hack not to use uninstalled xargs or find
 ls | grep -v app.py > to-be-removed.txt &&\
 for file in `cat to-be-removed.txt`; do rm $file; done

WORKDIR ${THOTH_GRAPH_SYNC_DIR}
