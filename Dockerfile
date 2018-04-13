FROM fedora:27

ENV \
 LANG=en_US.UTF-8 \
 THOTH_GRAPH_SYNC_DIR='/workdir'

LABEL io.k8s.description="Thoth Graph Sync Job" \
    io.k8s.display-name="Graph Sync" \
    io.openshift.tags="thoth,ai-stacks,janusgraph," \
    architecture=x86_64 \
    name="thoth-graph-sync-job" \
    vendor="Red Hat Office of the CTO - AI CoE" \
    license="GPLv3" 

RUN \
 dnf install -y gcc redhat-rpm-config python3-devel &&\
 mkdir -p ${THOTH_GRAPH_SYNC_DIR} &&\
 cd ${THOTH_GRAPH_SYNC_DIR} &&\
 pip3 install -r requirements.txt &&\
 # hack not to use uninstalled xargs or find
 ls | grep -v app.py > to-be-removed.txt &&\
 for file in `cat to-be-removed.txt`; do rm $file; done

COPY ./ ${THOTH_GRAPH_SYNC_DIR}

WORKDIR ${THOTH_GRAPH_SYNC_DIR}

CMD ["sync"]
ENTRYPOINT ["/workdir/app.py"]