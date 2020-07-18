import styles from "./Pantry.module.scss";
import { useSelector } from "react-redux";
import Ingredient from "./Ingredient";

export default function IngredientSearch(props) {
    let results = useSelector(state => state.query.results);
    return <>
            <div id={props.id} className={styles.queryBox}>
                <div className={styles.queryHover}>
                    {results.map((ingredient, idx) => (
                        <Ingredient searcher={props.searcher} idx={idx} name={ingredient.name} expiry={ingredient.expiry} category={ingredient.category}/>
                    ))}
                </div>
            </div>

    </>
}