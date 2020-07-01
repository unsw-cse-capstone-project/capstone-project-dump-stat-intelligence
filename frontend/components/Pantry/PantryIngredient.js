import styles from "./Pantry.module.scss";
import { useDispatch } from 'react-redux';


export default function PantryIngredient(props) {
    const dispatch = useDispatch();
    function cya(ingredient, category) {
        dispatch(props.func({ingredient : ingredient, category : category}));
    }

    return <span key={props.idx} className="tag is-dark">
        {props.ingredient}
        <button onClick={() => cya(props.ingredient, props.category)} className="delete is-small"/>
    </span>


}