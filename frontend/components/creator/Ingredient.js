import styles from "./Edit.module.scss";

import { useDispatch } from 'react-redux';
import { remove_ingredient } from "../../lib/redux/actions/createAction";

export default function Ingredient(props) {
    const dispatch = useDispatch();
    return <>
        <div key={props.idx} className={`tag ${styles.ingredient}`}>
            {`${props.ingredient.amount} ${props.ingredient.unit} ${props.ingredient.ingredient.name + (props.ingredient.adjective ? ", " + props.ingredient.adjective : "")}`}
            <button onClick={() => dispatch(remove_ingredient(props.idx))} className={`delete is-small`}/>
        </div>

    </>


}