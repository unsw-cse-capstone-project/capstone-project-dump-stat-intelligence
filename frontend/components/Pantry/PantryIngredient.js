import styles from "./Pantry.module.scss";
import { useState } from 'react';
import { useDispatch } from 'react-redux';


export default function PantryIngredient(props) {
    const [edit, setEdit] = useState(false);
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


    let editModal = null;
    if (edit) {
        console.log("YEET")
        editModal = <div className="modal is-active">
            <div className="modal-background" onClick={() => setEdit(false)} />
            <div className={`modal-content ${styles.box}`}>
                //CONTENT GOES HERE
            </div>
            <button className="modal-close is-large" aria-label="close" onClick={() => setEdit(false)}></button>
        </div> 
    }

    return <span key={props.idx} className={`tag ${close ? "is-danger" : "is-dark"}`}>
        {props.ingredient}
        {editModal}
<button onClick={() => {setEdit(true)}/*cya(props.ingredient, props.category)}*/} className="delete is-small"/>
    </span>


}