import styles from "./Edit.module.scss";
import { useSelector } from "react-redux";
import SearchIngredient from "./SearchIngredient";

export default function Searcher(props) {
    let results = useSelector(state => state.query.results);
    return <>
        <div id={props.id} className={styles.queryBox}>
            <div className={styles.queryHover}>
                {results.map((ingredient, idx) => (
                    <SearchIngredient func={props.func} searcher={props.searcher} idx={idx} name={ingredient.name} category={ingredient.category}/>
                ))}
            </div>
        </div>
    </>
} 