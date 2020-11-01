import os
import glob
import subprocess as sp

deps = glob.glob("**/deployment.yaml", recursive=True)
deps = [os.path.join('.', dep) for dep in deps]
print(deps)

for dep in deps:
    sp.run(f"kubectl apply -f".split(" ") + [dep])

svcs = glob.glob("**/service-nodeport.yaml", recursive=True)
svcs = [os.path.join('.', svc) for svc in svcs]
print(svcs)

for svc in svcs:
    sp.run(f"kubectl apply -f".split(" ") + [svc])
