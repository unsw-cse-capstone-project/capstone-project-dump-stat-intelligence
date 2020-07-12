import styles from "./Edit.module.scss";


import { useDispatch } from "react-redux";
import { clear_query } from "../../lib/redux/actions/queryAction";


export default function SearchIngredient(props) {
    const dispatch = useDispatch();
    function select() {
        props.func(props.name, props.category);
        document.getElementById(props.searcher).value = props.name;
        dispatch(clear_query());
    }
    return <div key={props.idx} onClick={select} className={styles.queryIngredient}>
        {props.name}
    </div>
}