import styles from "./Edit.module.scss";

import { useSelector, useDispatch } from "react-redux";
import Ingredient from "./Ingredient";

export default function IngredientEdit() {
    let ingredients = useSelector(state => state.create.ingredients);
    return <div>
        <div className="tags">
            {ingredients.map((item, idx) => (
                <Ingredient key={idx} idx={idx} ingredient={item}/>
            ))}
        </div>


    </div>
}