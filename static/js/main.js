// GET SEARCH FORM AND PAGE LINKS
let searchForm = document.getElementById("searchForm");
let pageLinks = document.getElementsByClassName("page-link");

console.log(pageLinks);

// ENSURE SEARCH FORM EXISTS
if (searchForm) {
  for (let i = 0; pageLinks.length > i; i++) {
    // console.log(pageLinks[i]);

    pageLinks[i].addEventListener("click", function (e) {
      e.preventDefault();
      // console.log("Button clicked");

      let page = this.dataset.page;
      // console.log("PAGE: ", page);

      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`;

      searchForm.submit();
    });
  }
}
