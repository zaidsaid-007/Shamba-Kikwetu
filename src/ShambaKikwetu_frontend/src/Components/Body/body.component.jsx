import './Body.style.css'
import Searchbox from "../search-box/search-box.component";
function Body() {
    return (
        <div>
         <h3 className="words">Land, where dreams take root and adventures unfold, a canvas of endless possibilities</h3>
            <div className="searchbox01"><Searchbox/></div>
        </div>
    );
}

export default Body;