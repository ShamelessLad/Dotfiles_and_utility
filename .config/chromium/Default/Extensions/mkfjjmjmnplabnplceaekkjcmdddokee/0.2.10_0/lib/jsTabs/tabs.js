function Tabs(a,b){this.html=document.querySelector(a),this.nav_links=this.html.querySelectorAll(".tabs_nav li a"),this.ontoggle_handlers_list={};var c=this;this.nav_links_array=function(){var a=[];return[].forEach.call(c.nav_links,function(b){a.push(b.hash)}),a}(),b&&this.onToggle(b),this.go_()}Tabs.prototype={fireOnToggle_:function(a){this.ontoggle_handlers_list.hasOwnProperty(a)&&this.ontoggle_handlers_list[a].length>0&&this.ontoggle_handlers_list[a].forEach(function(b){b(a)})},toggle:function(a){a&&-1!==this.nav_links_array.indexOf(a)&&([].forEach.call(this.html.querySelectorAll(".tabs_content>div"),function(b){b.style.display="#"+b.id===a?"block":"none"}),[].forEach.call(this.nav_links,function(b){b.hash===a?b.parentNode.classList.add("active"):b.parentNode.classList.remove("active")}),this.fireOnToggle_(a))},onToggle:function(a){function d(a,b){c.ontoggle_handlers_list[a]||(c.ontoggle_handlers_list[a]=[]),c.ontoggle_handlers_list[a].push(b)}var b,c=this;if("function"==typeof a)this.nav_links_array.forEach(function(b){d(b,a)});else if("object"==typeof a)for(b in a)-1!==this.nav_links_array.indexOf(b)&&d(b,a[b])},onNavClick_:function(){var a=this;a.html.querySelector(".tabs_nav").addEventListener("click",function(b){var d,c=b.target.hash;c||"LI"===b.target.tagName&&(d=b.target.querySelector("a"),c=d.hash),c&&-1!==a.nav_links_array.indexOf(c)&&!b.target.parentElement.classList.contains("active")&&a.toggle(c),b.preventDefault(),b.stopPropagation()},!1)},go_:function(){if(this.nav_links_array.length>0){var a=window.location.hash;a&&-1!==this.nav_links_array.indexOf(a)||(a=this.nav_links[0].hash),this.toggle(a),this.onNavClick_()}}};