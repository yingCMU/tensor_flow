## concepts
Haste is a system that maintains the **metadata about all static resources** in WWW and acts as a front-end for serving them to the users, [wiki](https://our.internmc.facebook.com/intern/wiki/Static_Resources/Haste/?breadcrumb_event=wiki_click_breadcrumb_direct_link)
https://our.internmc.facebook.com/intern/wiki/Static_Resources/Haste/Hitchhikers_Guide_To_Haste_Codebase/#staticresources-interfac
## two front-ends
There are two frontends to Haste, analyze_resources (production) and Ussr (sandboxes), but they both maintain the same underlying Haste data.
## codebase
(the majority of them are in flib/web/haste/ and flib/intern/web/haste/)
## dependencies
direct require: $root->getRequires();
all transitive dependencies: $map->getDependenciesForComponent

## haste in comet
https://our.internmc.facebook.com/intern/wiki/Comet/haste/
