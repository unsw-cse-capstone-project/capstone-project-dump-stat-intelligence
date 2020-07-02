import styles from "./Pantry.module.scss"

import { useDispatch } from "react-redux";
import { clear_query } from "../../lib/redux/actions/queryAction";
import { add } from "../../lib/redux/actions/pantryAction";

export default function Ingredient(props) {
    const dispatch = useDispatch();
    function newIn() {
        
        dispatch(add({name : props.name, category : props.category}));
        dispatch(clear_query());
        document.getElementById(props.searcher).value = null;
        

    }
    return (<div key={props.idx} onClick={newIn} className={styles.queryIngredient}>
        {props.name}
    </div>)
}