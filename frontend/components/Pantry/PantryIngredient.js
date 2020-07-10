import styles from "./Pantry.module.scss";
import { useDispatch } from 'react-redux';


export default function PantryIngredient(props) {
    const dispatch = useDispatch();
    function cya(ingredient, category) {
        dispatch(props.func({ingredient : ingredient, category : category}));
    }
    //CHECK TO SEE IF INGREDIENT IS CLOSE TO EXPIRING
    let close = false
    const now = new Date();
    
    if (props.expiry) {
        console.log(props.expiry)
        if ((props.expiry - now) / (1000 * 60 * 60 * 24) < 7) {

            close = true;
        }
    }
    return <span key={props.idx} className={`tag ${close ? "is-danger" : "is-dark"}`}>
        {props.ingredient}
        <button onClick={() => cya(props.ingredient, props.category)} className="delete is-small"/>
    </span>


}