import styles from "./Filter.module.scss";
import { useDispatch, useSelector } from 'react-redux';
import { explore_remove } from '../../lib/redux/actions/exploreAction';
import { load_expiry } from "../../lib/redux/actions/expiryAction";


export default function FilterIngredient(props) {
    const dispatch = useDispatch();
    const pantry = useSelector(state => state.pantry);
    const keys = Object.keys(pantry)
    function getInfo(ing) {
        for (var k of keys) {
            if (k !== 'meta') {
                for (var dict of pantry[k]) {
                    if (dict.name === ing) return dict;
                }
            }
        }
        return null;
    }


    let inPantry = pantry.meta.indexOf(props.ingredient) !== -1;
    let classTag = ""
    let info = null;
    if (inPantry) {
        info = getInfo(props.ingredient);
        if (info.expiry && (new Date(info.expiry) - new Date()) / (1000 * 60 * 60 * 24 ) < 7) classTag = styles.isExp;
        else classTag = styles.isIng;
    }
    
    function openEdit() {
        if (inPantry) {
            document.getElementById("expiry-edit").classList.toggle("is-active");
            dispatch(load_expiry(props.ingredient, info.category, info.expiry));
        }
    }

    return <span onClick={openEdit} key={props.idx} className={`tag ${styles.greyTag} ${classTag}`}>
        {props.ingredient}
      <button onClick={e => {e.stopPropagation(); dispatch(explore_remove({ingredient : props.ingredient}))}} className="delete is_small"></button>
    </span>
}