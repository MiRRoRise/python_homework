from enigma_machine import EnigmaMachine
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
import pytest

@pytest.fixture
def enigma_fixture():
    """Стандартная фикстура для создания машины"""
    rotor1 = Rotor("ZXCVBNMASDFGHJKLQWERTYUIOP", 'Q')
    rotor2 = Rotor("QWERTYUIOPASDFGHJKLZXCVBNM", 'T')
    rotor3 = Rotor("LMNOPQRSTUVWXYZABCDEFGHIJK",  'E')
    reflector = Reflector("YCBDEFGZIJKLMNOQPRTSUVWXAH")
    plugboard = Plugboard("AD BC")
    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)
    return enigma

@pytest.fixture
def enigma_fixture_identity():
    """Фикстура, которая аналогична стандартной"""
    rotor1 = Rotor("ZXCVBNMASDFGHJKLQWERTYUIOP", 'Q')
    rotor2 = Rotor("QWERTYUIOPASDFGHJKLZXCVBNM", 'T')
    rotor3 = Rotor("LMNOPQRSTUVWXYZABCDEFGHIJK",  'E')
    reflector = Reflector("YCBDEFGZIJKLMNOQPRTSUVWXAH")
    plugboard = Plugboard("AD BC")
    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)
    return enigma

@pytest.fixture
def enigma_fixture_other_positions_rotors():
    """Фикстура, которая аналогична стандартной, но за исключением иных положений роторов"""
    rotor1 = Rotor("ZXCVBNMASDFGHJKLQWERTYUIOP", 'G')
    rotor2 = Rotor("QWERTYUIOPASDFGHJKLZXCVBNM", 'H')
    rotor3 = Rotor("LMNOPQRSTUVWXYZABCDEFGHIJK",  'B')
    reflector = Reflector("YCBDEFGZIJKLMNOQPRTSUVWXAH")
    plugboard = Plugboard("AD BC")
    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)
    return enigma

@pytest.fixture
def enigma_fixture_other_rotor():
    """Фикстура, которая аналогична стандартной, но за исключением другого ротора"""
    rotor1 = Rotor("MASDFGHJKLQWERTYUIOPZXCVBN", 'Q')
    rotor2 = Rotor("QWERTYUIOPASDFGHJKLZXCVBNM", 'T')
    rotor3 = Rotor("LMNOPQRSTUVWXYZABCDEFGHIJK",  'E')
    reflector = Reflector("YCBDEFGZIJKLMNOQPRTSUVWXAH")
    plugboard = Plugboard("AD BC")
    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)
    return enigma

def test_initial_positions(enigma_fixture):
    """Тест на возможность выставления различных стартовых позиций роторов"""
    enigma = enigma_fixture
    assert enigma.rotors[0].pos == 16  # Положение ротора 1 (Q - 16)
    assert enigma.rotors[1].pos == 19  # Положение ротора 2 (T - 19)
    assert enigma.rotors[2].pos == 4 # Положение ротора 3 (E - 4)

def test_decoding(enigma_fixture, enigma_fixture_identity):
    """Тест на корректность расшифровки сообщения"""
    enigma_new = enigma_fixture
    enigma_old = enigma_fixture_identity
    text = "INTERESTED"

    # Шифрование
    encrypted_text = enigma_new.process(text)

    # Декодирование
    decoded_text = enigma_old.process(encrypted_text)

    assert text == decoded_text # Ожидается, что сообщение успешно расшифровано

def test_decoding_initial_positions(enigma_fixture, enigma_fixture_other_positions_rotors):
    """Тест на невозможность расшифровки при ином положении роторов"""
    enigma_default = enigma_fixture
    enigma_other_rotors = enigma_fixture_other_positions_rotors
    text = "INTERESTED"

    # Шифрование
    encrypted_text = enigma_default.process(text)

    # Дешифрование при помощи машины с иным расположением роторов
    decoded_text = enigma_other_rotors.process(encrypted_text)

    # Ожидается, что расшифрованное сообщение не совпадет с исходным
    assert text != decoded_text

def test_rotor_replace(enigma_fixture, enigma_fixture_other_rotor):
    """Тест на невозможность расшифровки при ином роторе"""
    enigma_default = enigma_fixture
    enigma_other_rotors = enigma_fixture_other_rotor
    text = "INTERESTED"

    # Шифрование
    encrypted_text = enigma_default.process(text)

    # Дешифрование при помощи машины с иным ротором
    decoded_text = enigma_other_rotors.process(encrypted_text)

    # Ожидается, что расшифрованное сообщение не совпадет с исходным
    assert text != decoded_text

# Параметризованный тест для проверки различных сообщений
@pytest.mark.parametrize("text", [
    "HELLO",
    "W",
    "TUESDAY",
    "TO BE OR NOT TO BE",
    "I AM ABSOLUTE"
])
def test_encoding_decoding_with_various_messages(enigma_fixture, enigma_fixture_identity, text):
    """Тест на корректность работы с разными сообщениями"""
    enigma_new = enigma_fixture
    enigma_old = enigma_fixture_identity

    # Шифрование
    encrypted_text = enigma_new.process(text)

    # Декодирование
    decoded_text = enigma_old.process(encrypted_text)

    assert text == decoded_text  # Ожидается, что сообщение успешно расшифровано

# Параметризованный тест для проверки некорректного ввода
@pytest.mark.parametrize("text", [
    "",  # Пустая строка
    "12345",  # Число
    "!@#$%",  # Специальные символы
    "joker", # Строчные буквы
    "ENIGMA123",  # Цифры после корректных заглавных букв
])
def test_invalid_input(enigma_fixture, text):
    """Тест на обработку некорректного ввода"""
    enigma = enigma_fixture
    # Ожидается выброс исключения
    with pytest.raises(ValueError):
        enigma.process(text)

if __name__ == "__main__":
    pytest.main()