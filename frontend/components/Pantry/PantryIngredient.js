import styles from "./Pantry.module.scss";
import { useDispatch } from 'react-redux';
import { load_expiry } from "../../lib/redux/actions/expiryAction";
import { explore_add } from "../../lib/redux/actions/exploreAction";

export default function PantryIngredient(props) {
    const dispatch = useDispatch();
    function cya(ingredient, category) {
        dispatch(props.func({ingredient : ingredient, category : category}));
    }
    //CHECK TO SEE IF INGREDIENT IS CLOSE TO EXPIRING
    let close = false
    const now = new Date();
    
    if (props.expiry) {
        let expires = new Date(props.expiry);
        if ((expires - now) / (1000 * 60 * 60 * 24) < 7) {

            close = true;
        }
    }

    function openEdit() {
        if (!props.del) {
            document.getElementById("expiry-edit").classList.toggle("is-active");
            dispatch(load_expiry(props.ingredient, props.category, props.expiry));
        }
    }
    return <div key={props.idx} className="control">
        <div className="tags has-addons">
            <span onClick={openEdit} className={`tag ${close ? "is-danger" : "is-dark"} ${styles.tag}`}>{props.ingredient}</span>
            {
                props.del ? 
                <a className="tag is-delete" onClick={(e) => {e.stopPropagation(); cya(props.ingredient, props.category)}}></a>
                : <a onClick={(e) => {e.stopPropagation(); dispatch(explore_add(props.ingredient))}} className="tag">
                    <span className="icon mdi mdi-dark">
                        <i className="fas fa-search-plus"></i>
                    </span>
                </a>
            }
        </div>
    </div>
    


}