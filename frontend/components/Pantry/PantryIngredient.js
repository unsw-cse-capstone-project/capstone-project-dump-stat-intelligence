import styles from "./Pantry.module.scss";
import { useDispatch } from 'react-redux';
import { load_expiry } from "../../lib/redux/actions/expiryAction";

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
        document.getElementById("expiry-edit").classList.toggle("is-active");
        dispatch(load_expiry(props.ingredient, props.category, props.expiry));
    }

    return <span onClick={openEdit} key={props.idx} className={`tag ${close ? "is-danger" : "is-dark"} ${styles.tag}`}>
        {props.ingredient}
        {
            props.del ? 
            <button onClick={(e) => {e.stopPropagation(); cya(props.ingredient, props.category)}} className="delete is-small"/>
            : ""
        }
    </span>


}