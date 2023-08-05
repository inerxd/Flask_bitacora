const body = document.querySelector("body"),
      sidebar = document.querySelector(".sidebar"),
      toggle = document.querySelector(".toggle"),
      searchBtn = body.querySelector(".search-box"),
      modeSwich = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");

toggle.addEventListener("click",()=>{
    sidebar.classList.toggle("close")
});

modeSwich.addEventListener("click",()=>{
    body.classList.toggle("dark");
    if(body.classList.contains("dark")){
        modeText.innerText = "Ligh Mode"
    }else{
        modeText.innerText = "Dark Mode"
    }
});