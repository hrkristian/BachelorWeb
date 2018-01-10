function currentLink() {
  var links = document.getElementsByClassName("nav_item");
  // console.log(links);

  for (var i = 0; i < links.length; i++) {
    if (links[i].href === window.location.href )
      links[i].id = "current_link";
  }
}
