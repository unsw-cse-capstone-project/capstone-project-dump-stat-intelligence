import styles from "./Pantry.module.scss";
import { useDispatch } from 'react-redux';
import { remove } from "../../lib/redux/actions/pantryAction";

export default function PantryIngredient(props) {
    const dispatch = useDispatch();
    function cya(ingredient, category) {
        dispatch(remove(ingredient, category));
    }

    return <span key={props.key} className="tag is-dark">
        {props.ingredient}
        <button onClick={() => cya(props.ingredient, props.category)} className="delete is-small"/>
    </span>


}