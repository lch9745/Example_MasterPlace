const add_data=document.querySelector("addData1");
const m_db=document.querySelector("Masterdb");

function paintdata(text)
{
    //<option value="none">{{ text }}</option>
}

function handleSubmit(event){
    //console.log("여기까진 실행되나2");
    event.preventDefault();
    const currentValue = add_data.value;
    paintdata(currentValue);
}

function init(){    
    //console.log("여긴 실행되나");        
    //add_data.addEventListener("submit", handleSubmit);
}

init();