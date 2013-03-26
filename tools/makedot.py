import dependencies

map=dependencies.get_dependencies("packages")

print "graph deps {"
for pkg in map.keys():
    for dep in map[pkg]:
        print "\t%s -> %s;" % (pkg,dep)
print "}"