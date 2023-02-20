kubectl get pods,svc
NAME                                   READY   STATUS    RESTARTS   AGE
pod/devops-time-app-7597d976fc-75wvl   1/1     Running   0          2m34s
pod/devops-time-app-7597d976fc-jlmfn   1/1     Running   0          2m34s
pod/devops-time-app-7597d976fc-rv9p7   1/1     Running   0          2m34s
pod/hello-node-67949d9db-779g8         1/1     Running   0          6m17s
pod/hello-world-75f87549d8-7fstd       1/1     Running   0          3m22s
pod/hello-world-75f87549d8-ftjzj       1/1     Running   0          3m22s
pod/hello-world-75f87549d8-k2qcc       1/1     Running   0          3m22s
pod/hello-world-75f87549d8-v9x2h       1/1     Running   0          3m22s
pod/hello-world-75f87549d8-zzkmp       1/1     Running   0          3m22s
pod/lab2app-7597d976fc-78qnq           1/1     Running   0          110s
pod/lab2app-7597d976fc-8lw5h           1/1     Running   0          110s
pod/lab2app-7597d976fc-g6dl8           1/1     Running   0          110s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   7m4s
PS C:\devops\repo\k8s>