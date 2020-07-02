import styles from "./Pantry.module.scss";
import { useSelector } from "react-redux";
import Ingredient from "./Ingredient";

export default function IngredientSearch(props) {
    let results = useSelector(state => state.query.results);
    return <>
        {
            results.length > 0 ?
            <div className={styles.queryBox}>
                <div className={styles.queryHover}>
                    {results.map((ingredient, idx) => (
                        <Ingredient searcher={props.searcher} idx={idx} name={ingredient.name} category={ingredient.category}/>
                    ))}
                </div>
            </div>
            : ""
        }

    </>
}