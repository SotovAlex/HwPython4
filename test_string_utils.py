import pytest
from string_utils import StringUtils

string_utilu = StringUtils

def test_capitilize_positive_lat():
    utils = StringUtils()
    res = utils.capitilize('hello')
    assert res == 'Hello'

def test_capitilize_positive_cir():
    utils = StringUtils()
    res = utils.capitilize('привет')
    assert res == 'Привет'

def test_capitilize_positive_num_as_string():
    utils = StringUtils()
    res = utils.capitilize('123')
    assert res == '123'

def test_capitilize_negative_space():
    utils = StringUtils()
    res = utils.capitilize('   ')
    assert res == '   '

def test_capitilize_negative_null():
    utils = StringUtils()
    res = utils.capitilize('')
    assert res == ''

def test_capitilize_positive_string_w_space():
    utils = StringUtils()
    res = utils.capitilize('hello world')
    assert res == 'Hello world'

def test_capitilize_negative_symbols():
    utils = StringUtils()
    res = utils.capitilize('#$#$')
    assert res == '#$#$'

def test_capitilize_positive_uppcase():
    utils = StringUtils()
    res = utils.capitilize('HELLO')
    assert res == 'Hello'

def test_capitilize_negative_int():
    utils = StringUtils()
    with pytest.raises(AttributeError):
        utils.capitilize(123)

def test_capitilize_negative_num():
    utils = StringUtils()
    with pytest.raises(TypeError):
        utils.capitilize()
    
def test_trim_lat():
    utils = StringUtils()
    res = utils.trim(' hello')
    assert res == 'hello'

def test_trim_cir():
    utils = StringUtils()
    res = utils.trim(' привет')
    assert res == 'привет'

def test_trim_positive_num_as_string():
    utils = StringUtils()
    res = utils.trim(' 1235')
    assert res == '1235'

def test_trim_positive_stping_w_space():
    utils = StringUtils()
    res = utils.trim(' hello world')
    assert res == 'hello world'

def test_trim_positive_5space():
    utils = StringUtils()
    res = utils.trim('     hello')
    assert res == 'hello'

def test_trim_positive_10space():
    utils = StringUtils()
    res = utils.trim('          hello')
    assert res == 'hello'

def test_trim_negative_null():
    utils = StringUtils()
    res = utils.trim('')
    assert res == ''

def test_trim_negative_space():
    utils = StringUtils()
    res = utils.trim(' ')
    assert res == ''

def test_trim_negative_int():
    utils = StringUtils()
    with pytest.raises(AttributeError):
        res = utils.trim( 123)

def test_trim_negative_none():
    utils = StringUtils()
    with pytest.raises(TypeError):
        res = utils.trim()    

def test_to_list_positive_lat():
    utils = StringUtils()
    res = utils.to_list('a,b,c,d')
    assert res == ['a', 'b', 'c', 'd']

def test_to_list_positive_cir():
    utils = StringUtils()
    res = utils.to_list('а,б,в,г')
    assert res == ['а', 'б', 'в', 'г']

def test_to_list_positive_num():
    utils = StringUtils()
    res = utils.to_list('1,2,3,4')
    assert res == ['1', '2', '3', '4']

def test_to_list_positive_w_delim():
    utils = StringUtils()
    res = utils.to_list('a^b^c^d', '^')
    assert res == ['a', 'b', 'c', 'd']

def test_to_list_positive_wo_delim():
    utils = StringUtils()
    res = utils.to_list('a,b,c,d', ':')
    assert res == ['a,b,c,d']

def test_to_list_negative_null():
    utils = StringUtils()
    res = utils.to_list('')
    assert res == []

def test_to_list_negative_space():
    utils = StringUtils()
    res = utils.to_list(' ')
    assert res == []

def test_to_list_positive_delim_space():
    utils = StringUtils()
    res = utils.to_list('a b c d', ' ')
    assert res == ['a', 'b', 'c', 'd']

def test_to_list_positive_w_null_in_delim():
    utils = StringUtils()
    res = utils.to_list(',,,')
    assert res == ['', '', '', '']

def test_to_list_positive_w_space_in_delim():
    utils = StringUtils()
    res = utils.to_list(' , , , ')
    assert res == [' ', ' ', ' ', ' ']


def test_to_list_negative_none():
    utils = StringUtils()
    with pytest.raises(TypeError):
        res = utils.to_list()
    
def test_to_list_negative_no_string():
    utils = StringUtils()
    with pytest.raises(NameError):
        res = utils.to_list(a,b,c,d)

def test_to_list_negative_int():
    utils = StringUtils()
    with pytest.raises(TypeError):
        res = utils.to_list(1,2,3,4)

def test_contains_positive_eng_uppcase_true():
    utils = StringUtils()
    res = utils.contains('Hello World', 'W')
    assert res == True

def test_contains_positive_cir_false():
    utils = StringUtils()
    res = utils.contains('Привет мир', 'к')
    assert res == False

def test_contains_positive_num():
    utils = StringUtils()
    res = utils.contains('Hell0 W0rld', '0')
    assert res == True

def test_contains_positive_space():
    utils = StringUtils()
    res = utils.contains('Hello World', ' ')
    assert res == True

def test_contains_negative_symbol_none():
    utils = StringUtils()
    res = utils.contains('Hello World', '')
    assert res == False

def test_delete_symbol_positive_eng_uppcase():
    utils = StringUtils()
    res = utils.delete_symbol('Hello World', 'W')
    assert res == 'Hello orld'

def test_delete_symbol_positive_space():
    utils = StringUtils()
    res = utils.delete_symbol('Hello World', ' ')
    assert res == 'HelloWorld'

def test_delete_symbol_positive_symbol_none():
    utils = StringUtils()
    res = utils.delete_symbol('Hello World', '')
    assert res == 'Hello World'

def test_delete_symbol_positive_cir():
    utils = StringUtils()
    res = utils.delete_symbol('Привет Мир', 'и')
    assert res == 'Првет Мр'

def test_delete_symbol_positive_num():
    utils = StringUtils()
    res = utils.delete_symbol('Hello 2World3', '2')
    assert res == 'Hello World3'

def test_delete_symbol_positive_symbols():
    utils = StringUtils()
    res = utils.delete_symbol('Hello World!', 'rld!')
    assert res == 'Hello Wo'

def test_starts_with_eng_uppcase_true():
    utils = StringUtils()
    res = utils.starts_with('Hello World', 'H')
    assert res == True

def test_starts_with_cir_false():
    utils = StringUtils()
    res = utils.starts_with('Привет мир', 'к')
    assert res == False

def test_starts_with_positive_num():
    utils = StringUtils()
    res = utils.starts_with('0Hell0 W0rld', '0')
    assert res == True

def test_starts_with_positive_space():
    utils = StringUtils()
    res = utils.starts_with(' Hello World', ' ')
    assert res == True

def test_starts_with_negative_symbol_none():
    utils = StringUtils()
    res = utils.starts_with('Hello World', '')
    assert res == False

def test_end_with_eng_uppcase_true():
    utils = StringUtils()
    res = utils.end_with('Hello WorlD', 'D')
    assert res == True

def test_end_with_cir_false():
    utils = StringUtils()
    res = utils.end_with('Привет мир', 'к')
    assert res == False

def test_end_with_positive_num():
    utils = StringUtils()
    res = utils.end_with('0Hell0 World0', '0')
    assert res == True

def test_end_with_positive_space():
    utils = StringUtils()
    res = utils.end_with(' Hello World ', ' ')
    assert res == True

def test_end_with_negative_symbol_none():
    utils = StringUtils()
    res = utils.end_with('Hello World', '')
    assert res == False

def test_is_empty_positive_true():
    utils = StringUtils()
    res = utils.is_empty('')
    assert res == True

def test_is_empty_positive_cyr_false():
    utils = StringUtils()
    res = utils.is_empty('Привет мир')
    assert res == False

def test_is_empty_positive_num():
    utils = StringUtils()
    res = utils.is_empty('0')
    assert res == False

def test_is_empty_positive_space():
    utils = StringUtils()
    res = utils.is_empty(' ')
    assert res == True

def test_list_to_string_positive_lat():
    utils = StringUtils()
    res = utils.list_to_string(['a','b','c','d'])
    assert res == ('a, b, c, d')

def test_list_to_string_positive_cir():
    utils = StringUtils()
    res = utils.list_to_string(['а','б','в','г'])
    assert res == ('а, б, в, г')

def test_list_to_string_positive_num():
    utils = StringUtils()
    res = utils.list_to_string(['1','2','3','4'])
    assert res == ('1, 2, 3, 4')

def test_list_to_string_positive_w_delim():
    utils = StringUtils()
    res = utils.list_to_string(['a','b','c','d'], '^')
    assert res == ('a^b^c^d')

def test_list_to_string_positive_wo_delim():
    utils = StringUtils()
    res = utils.list_to_string(['a','b','c','d'], '')
    assert res == ('abcd')

def test_list_to_string_positive_int():
    utils = StringUtils()
    res = utils.list_to_string([1,2,3,4])
    assert res == ('1, 2, 3, 4')

def test_list_to_string_negative_space():
    utils = StringUtils()
    res = utils.list_to_string([' '])
    assert res == (' ')

def test_list_to_string_positive_joiner_space():
    utils = StringUtils()
    res = utils.list_to_string(['a', 'b', 'c', 'd'], ' ')
    assert res == ('a b c d')

def test_list_to_string_positive_null_joiner_simbol():
    utils = StringUtils()
    res = utils.list_to_string(['','','',''], '&')
    assert res == ('&&&')

def test_list_to_string_positive_w_space():
    utils = StringUtils()
    res = utils.list_to_string([' ',' ',' ',' '], '@')
    assert res == (' @ @ @ ')