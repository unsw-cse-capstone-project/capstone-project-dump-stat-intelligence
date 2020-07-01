import { combineReducers } from 'redux';
import { authReducer } from './authReducer';
import { pantryReducer } from './pantryReducer';


export default combineReducers({
    auth : authReducer,
    pantry : pantryReducer
});