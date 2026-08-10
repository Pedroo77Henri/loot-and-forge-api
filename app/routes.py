from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Item, Status, Raridade, TipoItem
from pydantic import BaseModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Itens(BaseModel):
    nome: str
    tipo: TipoItem
    raridade: Raridade
    poder: int

@router.post("/itens")
def criar_item(info: Itens, db: Session = Depends(get_db)):
    nome_info = info.nome
    tipo_info = info.tipo
    raridade_info = info.raridade
    poder_info = info.poder

    new_item = Item(
        nome = nome_info,
        tipo = tipo_info,
        raridade = raridade_info,
        poder = poder_info,
        status = Status.PRONTO

    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return {
            "Mensagem": "Item criado",
            "nome": nome_info,
            "tipo": tipo_info,
            "raridade": raridade_info,
            "poder": poder_info,
            "status": Status.PRONTO
        }
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Errao ao salvar no banco por dado errado")




class Info(BaseModel):
    nome: str
    tempo_necessario: int

@router.post("/itens/forjar")
def info_itens(informacao: Info, db: Session = Depends(get_db)):
    entrada_nome = informacao.nome
    entrada_tempo = informacao.tempo_necessario

    novo_item = Item(
        nome = entrada_nome,
        tempo_necessario = entrada_tempo,
        status = Status.FORJANDO,
        tipo = TipoItem.ARMA,
        raridade = Raridade.COMUM,
        poder = 10
    )

    try:
        db.add(novo_item)
        db.commit()
        db.refresh(novo_item)

        return {
            "mensagem": "Item colocado na forja com sucesso",
            "item": {
                "id": novo_item.id,
                "nome": novo_item.nome,
                "status": novo_item.status.value,
                "criado_em": novo_item.criado_em

            }
        }
    except Exception:
        db.rollback()
        raise HTTPException (status_code=500, detail="Erro ao salvar item")


@router.get("/itens/{search_id}")
def search_item(search_id: int, db: Session = Depends(get_db)):
    search = db.query(Item).filter(Item.id == search_id).first()
    if search is None:
        raise HTTPException(status_code=404, detail="ID não encontrado.")
    return search

@router.delete("/itens/{delete_id}")
def delete_item(delete_id: int, db: Session = Depends(get_db)):
    delete = db.query(Item).filter(Item.id == delete_id). first()
    if delete is None:
        raise HTTPException(status_code=404, detail="Não foi possível deletar pois o ID não foi encontrado")
    try:
        db.delete(delete)
        db.commit()
        return {"Item": f"{delete.nome} removido"}
    except Exception:
        raise HTTPException(status_code=500, detail="Não foi possível remover o item")
