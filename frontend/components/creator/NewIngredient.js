import styles from "./Edit.module.scss";

import Modal from "../modal/Modal";

import { create_ingredient } from "../../lib/redux/actions/createAction";

export default function NewIngredient(props) {
    const newIn = (e) => {
        e.preventDefault();
        create_ingredient(e.target.elements.name.value, {name: e.target.elements.category.value})
        document.getElementById(props.id).classList.toggle("is-active");
    }
    let content = <form onSubmit={newIn}>
        <h3 className="title is-3">Add ingredient to database</h3>
        <label className="label">Ingredient Name</label>
        <div className="field control">
            <input required={true} name="name" className="input" type="text" placeholder="name"/>
        </div>
        <label className="label">Category</label>
        <div className="field control">
            <div style={{width:"100%"}} className="select">
                <select name="category" style={{width:"100%"}}>
                    <option>Tins and jars</option>
                    <option>Spreads and toppings</option>
                    <option>Spices and seasonings</option>
                    <option>Rics, grains and pasta</option>
                    <option>Oils, dressings and vinegars</option>
                    <option>Nuts</option>
                    <option>Meats</option>
                    <option>Fruits and vegetables</option>
                    <option>Dairy and eggs</option>
                    <option>Breads and pastry</option>
                    <option>Beverages</option>
                    <option>Baking</option>
                </select>
            </div>
        </div>
        <div className="field control">
            <button type="submit" className="button is-primary">Commit Ingredient</button>
        </div>

    </form>
    return <Modal id={props.id} content={content}/>
}