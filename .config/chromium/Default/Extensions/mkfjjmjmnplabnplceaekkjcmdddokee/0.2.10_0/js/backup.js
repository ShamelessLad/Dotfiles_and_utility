var backup={storage_area:chrome.storage.sync,getStoredKeys:function(a){var b=[];this.storage_area.get(function(c){var d;for(d in c)(0===d.indexOf("tg_")||storage.default_options.hasOwnProperty(d))&&b.push(d);a(b)})},getBackupData:function(a){var b=this;this.getStoredKeys(function(c){b.storage_area.get(c,function(b){a(JSON.stringify(b))})})},cleanupBeforeReplace:function(a){var b=this;this.getStoredKeys(function(c){b.storage_area.remove(c,function(){a(chrome.runtime.lastError)})})},replaceFromBackup:function(a,b){var c,d=this.storage_area;try{c=JSON.parse(a)}catch(e){b("error")}c&&"object"==typeof c&&this.cleanupBeforeReplace(function(a){a?b(a):d.set(c,function(){b(chrome.runtime.lastError)})})}};