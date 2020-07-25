import styles from "./Pantry.module.scss"

import { useDispatch } from "react-redux";
import { clear_query } from "../../lib/redux/actions/queryAction";
import { clear_search } from "../../lib/redux/actions/searchAction";
import { add } from "../../lib/redux/actions/pantryAction";
import { explore_add } from "../../lib/redux/actions/exploreAction";

export default function Ingredient(props) {
    
    
    const dispatch = useDispatch();
    function newIn() {
        if (props.runningList) {
            dispatch(explore_add(props.name));
            dispatch(clear_search());
        } else {
            dispatch(add({name : props.name, category : props.category, expiry : props.expiry}));
            dispatch(clear_query());
        }
        document.getElementById(props.searcher).value = null;
    }
    
    return (<div key={props.idx} onClick={newIn} className={styles.queryIngredient}>
        {props.name}
    </div>)
}