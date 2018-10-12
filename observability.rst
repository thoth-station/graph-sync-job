Observabinity
=============

This section describes a set of metrics exported by each Graph Sync Job run.

After each graph sync job has finished, it will export a few metrics to a Prometheus push gateway. This will happen if the job has set the environment variable `THOTH_METRICS_PUSHGATEWAY_URL`. The template `openshift/cronJob-template.yaml` sets the env var to a value referenced in the ConfigMap `thoth`.

Exported Metrics
----------------

The following table shows all the metrics exported by the graph sync job.

.. csv-table:: Graph Sync Job Metrics
   :header: "Metric", "Job Name", "Description"

    graph_sync_job_runtime_seconds,  graph-sync,  Runtime of graph sync job in seconds.
    graph_sync_solver_results_processed,  graph-sync,  Solver results processed.
    graph_sync_solver_results_synced,  graph-sync,  Solver results synced.
    graph_sync_solver_results_skipped,  graph-sync,  Solver results skipped processing.
    graph_sync_solver_results_failed,  graph-sync,  Solver results failed processing.
    graph_sync_analysis_results_processed,  graph-sync,  Analysis results processed. 
    graph_sync_analysis_results_synced,  graph-sync,  Analysis results synced.
    graph_sync_analysis_results_skiped,  graph-sync,  Analysis results skipped processing.
    graph_sync_analysis_results_failed,  graph-sync,  Analysis results failed processing. 